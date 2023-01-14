#if __linux__
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#endif

#include "bme68x_defs.h"

#define BME680_I2C_ADDR_PRIMARY		UINT8_C(0x76)
#define BME680_I2C_ADDR_SECONDARY	UINT8_C(0x77)

class I2CConnection
{
public:
    I2CConnection()
    {}

    int i2cFid() { return _i2cFid; }
    int i2cAddress() { return _i2cAddress; }

    bool isOpen() { return (_i2cFid >= 0); }

    bool i2cOpen()
    {
        #if __linux__
        if (isOpen()) {
            return true;
        }
        _i2cFid = open("/dev/i2c-1", O_RDWR);
        bool success = (_i2cFid >= 0);
        if (success) {
            i2cSetAddress();
        }
        return success;
        #else
        return true;
        #endif
    }

    void i2cClose()
    {
        #if __linux__
        close(_i2cFid);
        #endif
        _i2cFid = -1;
    }

private:

    bool i2cSetAddress()
    {
        #if __linux__
        if (isOpen() && ioctl(_i2cFid, I2C_SLAVE, _i2cAddress) < 0) {
            return false;
        }
        #endif
        return true;
    }

    int _i2cFid = -1;
    int _i2cAddress = BME680_I2C_ADDR_PRIMARY;
};