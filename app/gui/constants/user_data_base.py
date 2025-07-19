def ClearUserData():
    return {
            "load_spec" : {
                "rated_voltage" : None,
                "active_power": None,
                "reactive_power" : None,
                "load_type" : None
            },
           "type_env" : {
                "env_temp" : 0.0,
                "cable_type": "Single Core",
                "placement" : "Flat"
           },
           "cable_selection": {
               "cable_id" : None
               
           },
           "cable_length": {
               "length" : None,
               "number_of_parallel_circuits" : None
           }
        }