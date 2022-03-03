#include "influxdb_client.h"

std::string InfluxClient::getEnv(std::string key)
{
    char *val = getenv(key.c_str());
    return val == NULL ? std::string("") : std::string(val);
}