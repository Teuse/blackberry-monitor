#include <iostream>

class InfluxClient
{
    InfluxDbClient()
    {
    }

private:
    std::string getEnv(std::string key);
};
