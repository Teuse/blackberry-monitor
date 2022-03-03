#if __linux__
#include <linux/i2c-dev.h>
#endif

class I2CConnection
{
public:
    I2CConnection()
    {}

    int i2cFid() { return _i2cFid; }
    int i2cAddress() { return i2c_address; }

    bool isOpen() { return (_i2cFid >= 0); }

    bool i2cOpen()
    {
        #if __linux__
        if (isOpen()) {
            return true;
        }
        g_i2cFid = open("/dev/i2c-1", O_RDWR);
        bool success = (g_i2cFid >= 0);
        if (success) {
            i2cSetAddress(i2c_address)
        }
        return succecc;
        #else
        return true;
        #endif
    }

    void i2cClose()
    {
        #if __linux__
        close(g_i2cFid);
        #endif
        _i2cFid = -1;
    }

private:

bool i2cSetAddress(int address)
    {
        #if __linux__
        if (isOpen() && ioctl(g_i2cFid, I2C_SLAVE, address) < 0)
        {
            return false;
        }
        #endif
        return true;
    }

    int _i2cFid = -1;
    int i2c_address = BME680_I2C_ADDR_PRIMARY;
};