from typing import Callable
import asyncio
import logging


class async_runner:
    on_closes = []

    def exeute_on_close(self):
        try:
            for fn in self.on_closes:
                try:
                    fn()
                except KeyboardInterrupt:
                    continue
                except BaseException as e:
                    logging.exception(e.with_traceback(None), stack_info=True)
        except:
            pass

    def on_close_function(self, fn: Callable):
        self.on_closes.append(fn)
        return fn

    async def close_check_task(self):
        while True:
            try:
                has_no_finished_task = False
                cur_task = asyncio.current_task(self.loop)
                for task in asyncio.all_tasks(self.loop):
                    if cur_task == task or task.done():
                        continue
                    has_no_finished_task = True
                    break

                if not has_no_finished_task:
                    return

                await asyncio.sleep(1, loop=self.loop)
            except:
                pass

    def run_forever(self, loop: asyncio.BaseEventLoop = asyncio.get_event_loop()):
        self.loop = loop
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.exeute_on_close()
            self.loop.run_until_complete(self.close_check_task())
            self.loop.stop()
            self.loop.close()
        except BaseException as e:
            logging.exception(e.with_traceback(None), stack_info=True)
            return


g_async_runner = async_runner()


def on_close_function(fn: Callable):
    return g_async_runner.on_close_function(fn)
