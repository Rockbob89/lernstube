import inspect

def make_tag(tag, *children, **attrs):
    ret = f"<{tag} "


    for k,v in attrs.items():
        ret += f"{k.rstrip('_')}=\"{v}\" " 

    ret = ret.rstrip()

    if len(children) == 0:
        ret = f"{ret} />"
        return ret
    ret = f"{ret.rstrip()}>"

    for child in children:      
        ret+= f"{child} "
    
    ret = f"{ret.rstrip()}</{tag}>"

    return ret

def merge_configs(*configs, **overrides):
    ret = {}
    for config in configs:
        for k,v in config.items():
            ret[k] = v
    
    for k,v in overrides.items():
        ret[k] = v
    return ret

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def call_with_matching_args(func, **kwargs):
    funcParams = inspect.signature(func).parameters
    call = {}
    for k,v in kwargs.items():
        if k in funcParams:
            call[k] = v

    return  func(**call)
    

mytag = make_tag("div", "hello", "world", class_="container", id="main")
myconfigs = merge_configs({"a": 1}, {"b": 2, "a": 3}, c=4)
mykwargs = call_with_matching_args(greet, name="Alice", greeting="Hi", age=30)

print(mytag)
print(myconfigs)
print(mykwargs)