
def data_type(arg_type=None):
    if isinstance(arg_type,str):
        return len(arg_type)
    elif arg_type==None:
        return "no value"
    elif isinstance(arg_type,bool):
        return arg_type
    elif isinstance(arg_type,int):
        if arg_type == 6:
            return "andela"
        if arg_type>100:
            return "more than 100"
        if arg_type <100:
            return "less than 100"
        if arg_type ==100:
            return "equal to 100"

    elif isinstance(arg_type,list):
        if len(arg_type)>=3:
            return arg_type[2]
        else: 
          return None

    else: 
      return





