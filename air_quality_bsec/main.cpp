#include <iostream>
#include <bme680.h>
#include <bsec_interface.h>
#include <bsec_datatypes.h>

void i2cOpen()
{
  g_i2cFid = open("/dev/i2c-1", O_RDWR);
  if (g_i2cFid < 0) {
    perror("i2cOpen");
    exit(1);
  }
}

int main(int argc, char *argv[])
{
   std::cout << "Hallo BME" << std::endl;
   i2cOpen();
   return 0;
}
