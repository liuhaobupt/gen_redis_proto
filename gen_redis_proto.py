def gen_redis_proto(*cmd):
    proto = ""
    proto = "*"+str(len(cmd))+"\r\n"
    for arg in cmd:
        proto += "$"+str(len(arg))+"\r\n"
        proto += arg+"\r\n"
    return proto

if __name__ == "__main__": 
    print gen_redis_proto("SET","mykey","Hello world!")

