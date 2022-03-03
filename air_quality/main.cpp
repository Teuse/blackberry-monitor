#include <iostream>
#include <unistd.h>
#include <sys/stat.h>
#include <bsec_datatypes.h>
#include <bsec_integration.h>

#include "i2c_connection.h"


I2CConnection i2cCon = I2CConnection();

float tempOffset = 5.0f;
auto sampleRateMode = BSEC_SAMPLE_RATE_LP;
std::string filenameState = "/etc/airquality/bsec_iaq.state";
std::string filenameConfig = "/etc/airquality/bsec_iaq.config";

int8_t bus_write(uint8_t dev_addr, uint8_t reg_addr, uint8_t *reg_data_ptr, uint16_t data_len)
{
  int8_t rslt = 0; /* Return 0 for Success, non-zero for failure */

  uint8_t reg[16];
  reg[0]=reg_addr;

  for (int i=1; i<data_len+1; i++)
    reg[i] = reg_data_ptr[i-1];

  if (write(i2cCon.i2cFid(), reg, data_len+1) != data_len+1) {
    perror("user_i2c_write");
    rslt = 1;
    exit(1);
  }

  return rslt;
}

int8_t bus_read(uint8_t dev_addr, uint8_t reg_addr, uint8_t *reg_data_ptr, uint16_t data_len)
{
  int8_t rslt = 0; /* Return 0 for Success, non-zero for failure */

  uint8_t reg[1];
  reg[0]=reg_addr;

  if (write(i2cCon.i2cFid(), reg, 1) != 1) {
    perror("user_i2c_read_reg");
    rslt = 1;
  }

  if (read(i2cCon.i2cFid(), reg_data_ptr, data_len) != data_len) {
    perror("user_i2c_read_data");
    rslt = 1;
  }

  return rslt;
}

void sleep_ms(uint32_t t_ms)
{
  struct timespec ts;
  ts.tv_sec = 0;
  /* mod because nsec must be in the range 0 to 999999999 */
  ts.tv_nsec = (t_ms % 1000) * 1000000L;
  nanosleep(&ts, NULL);
}

int64_t get_timestamp_us()
{
  struct timespec spec;
  //clock_gettime(CLOCK_REALTIME, &spec);
  /* MONOTONIC in favor of REALTIME to avoid interference by time sync. */
  clock_gettime(CLOCK_MONOTONIC, &spec);

  int64_t system_current_time_ns = (int64_t)(spec.tv_sec) * (int64_t)1000000000
                                   + (int64_t)(spec.tv_nsec);
  int64_t system_current_time_us = system_current_time_ns / 1000;

  return system_current_time_us;
}

void output_ready(int64_t timestamp, float iaq, uint8_t iaq_accuracy, float temperature, float humidity,
     float pressure, float raw_temperature, float raw_humidity, float gas, bsec_library_return_t bsec_status,
     float static_iaq, float co2_equivalent, float breath_voc_equivalent)
{
  time_t t = time(NULL);
  struct tm tm = *localtime(&t);

  std::cout << "IAQ (accuracy): " << iaq << " (" << iaq_accuracy << ")" << std::endl;
  std::cout << "Temperature:     " << temperature << std::endl;
  std::cout << "Humidity:        " << humidity << std::endl;
  std::cout << "Pressure:        " << pressure / 100 << std::endl;
  std::cout << "Gas:             " << gas << std::endl;
  std::cout << "Status:          " << bsec_status << std::endl;
}

uint32_t binary_load(uint8_t *b_buffer, uint32_t n_buffer, const char* filename,
                     uint32_t offset)
{
  int32_t copied_bytes = 0;
  int8_t rslt = 0;

  struct stat fileinfo;
  rslt = stat(filename, &fileinfo);
  if (rslt != 0) {
    perror("stat'ing binary file");
    return 0;
  }

  uint32_t filesize = fileinfo.st_size - offset;

  if (filesize > n_buffer) {
    fprintf(stderr,"%s: %d > %d\n", "binary data bigger than buffer", filesize,
            n_buffer);
    return 0;
  } else {
    FILE *file_ptr;
    file_ptr = fopen(filename,"rb");
    if (!file_ptr) {
      perror("fopen");
      return 0;
    }
    fseek(file_ptr,offset,SEEK_SET);
    copied_bytes = fread(b_buffer,sizeof(char),filesize,file_ptr);
    if (copied_bytes == 0) {
      fprintf(stderr,"%s\n","binary_load");
    }
    fclose(file_ptr);
    return copied_bytes;
  }
}

uint32_t state_load(uint8_t *state_buffer, uint32_t n_buffer)
{
  int32_t rslt = 0;
  rslt = binary_load(state_buffer, n_buffer, filenameState.c_str(), 0);
  return rslt;
    return 0;
}

void state_save(const uint8_t *state_buffer, uint32_t length)
{
  FILE *state_w_ptr;
  state_w_ptr = fopen(filenameState.c_str(),"wb");
  fwrite(state_buffer,length,1,state_w_ptr);
  fclose(state_w_ptr);
}

uint32_t config_load(uint8_t *config_buffer, uint32_t n_buffer)
{
  int32_t rslt = binary_load(config_buffer, n_buffer, filenameConfig.c_str(), 4);
  return rslt;
}

int main()
{
  if (!i2cCon.i2cOpen()) {
    std::cout << "Failed to open i2c bus" << std::endl;
    return -1;
  }

  return_values_init ret = bsec_iot_init(sampleRateMode, tempOffset, bus_write, bus_read,
                      sleep_ms, state_load, config_load);
  if (ret.bme680_status) {
    return (int)ret.bme680_status;
  } else if (ret.bsec_status) {
    return (int)ret.bsec_status;
  }

  bsec_iot_loop(sleep_ms, get_timestamp_us, output_ready, state_save, 10000);

  i2cCon.i2cClose();
  return 0;
}

