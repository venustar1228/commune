

import commune


class API(commune.Module):
    def __init__(self, module:str = 'module', refresh=False):

        self.build(refresh=refresh)
        self.module = commune.connect('module')
        self.merge(self.module)
        
    @classmethod
    def deploy_api(cls, refresh:bool = True):
        commune.launch(name='module', mode='ray', refresh=refresh)
        
    @classmethod
    def serve_api(cls):
        return commune.get_actor('module').serve(ray_get=False)
    
    @classmethod
    def build(cls, refresh:bool=True):
        if not cls.actor_exists('module') or refresh:
            commune.cmd('python3 commune/api.py -fn deploy_api -args "[\'True\']"')
        
        module = commune.get_actor('module')
        if not module.server_running():
            module.serve(ray_get=False)
            import time
            time_elapsed = 0
            while True:
                time.sleep(1)
                time_elapsed += 1
                server_running = module.server_running()
                commune.print(f'Is Server Running {server_running} Time Elapsed: {time_elapsed}', color='yellow')
                if server_running:
                    break
            
            commune.print(f'COMMUNE IS SERVED {server_running}', color='green')

        
    
    @classmethod
    def run(cls): 
        args = cls.argparse()

        if args.function in ['deploy_api',  'serve_api', 'build']:
            obj = cls
        else:
            obj = cls().module
            
        output =getattr(obj, args.function)(*args.args, **args.kwargs)  
        commune.print(output, 'green')


if __name__ == "__main__":
    API.run()
    
