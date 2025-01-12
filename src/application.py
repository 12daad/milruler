import tkinter as tk
import keyboard
import mouse

from util import WeaponAccessory

class Application:
    def start(self):
        pass

    def run(self):
        self.tk_root.mainloop()

    def __init__(self):
        self.accessory:WeaponAccessory = WeaponAccessory.WEAPON_ACCESSORY_LIST[0]
        self.tk_root, self.top, self.tk_canvas, screen_width, screen_height = self._init_tk()
        self.tk_center = (screen_width/2, screen_height/2)
        self.tk_bead = self.tk_canvas.create_oval(screen_width/2-2, 
                                  screen_height/2-2, 
                                  screen_width/2+2, 
                                  screen_height/2+2, 
                                  outline='red')
        self.label = self.tk_canvas.create_text(screen_width/2+100, screen_height/2, text="0 m", fill="blue")
        self.current_dist = 0

        self._init_keyboard()
        self._init_mouse()


    def _init_tk(self) -> tuple[tk.Tk, tk.Toplevel, tk.Canvas, int, int]:
        # 创建主窗口
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口

        # 创建一个无边框的顶级窗口
        top = tk.Toplevel(root)
        top.overrideredirect(True)  # 去掉窗口边框
        top.attributes("-topmost", True)  # 窗口置顶
        top.attributes("-transparentcolor", "white")  # 设置透明色

        # 获取屏幕分辨率
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()

        # 设置窗口大小
        canvas = tk.Canvas(top, 
                        width=screen_width, 
                        height=screen_height, 
                        bg="white", 
                        highlightthickness=0)
        canvas.pack()
        
        return root, top, canvas, screen_width, screen_height

    def _init_keyboard(self):
        #  left: -100 meter
        keyboard.add_hotkey(hotkey='left', 
                            callback=self._global_event_callback, 
                            args= [-100]
                            )
        #  right: 100 meter
        keyboard.add_hotkey(hotkey='right', 
                            callback=self._global_event_callback, 
                            args= [100]
                            )
        #  up: 50 meter
        keyboard.add_hotkey(hotkey='up', 
                            callback=self._global_event_callback, 
                            args= [50]
                            )
        #  down: -50 meter
        keyboard.add_hotkey(hotkey='down', 
                            callback=self._global_event_callback, 
                            args= [-50]
                            )
        #  choose accessory
        keyboard.add_hotkey(hotkey='up+down', 
                            callback=self.choose_accessory
                            )

    def _init_mouse(self):
        def on_scrool(event):
            if isinstance(event, mouse.WheelEvent):
                self._global_event_callback(event.delta*50)
    
        mouse.hook(on_scrool)

    def _global_event_callback(self, delta_dist):
        self.current_dist += delta_dist
        
        # 设置 tk_bead 的位置
        x, y = self.bead_xy
        sz = self.bead_size
        delta_y = self.accessory.calculate_correcting(delta_dist)
        self.set_bead((x, y+delta_y), 
                        sz)
        
        # 设置 tk_label 的位置
        x, y = self.label_xy
        delta_y = self.accessory.calculate_correcting(delta_dist)
        self.set_label((x, y+delta_y), f"{self.current_dist} m")
        
        # 打印信息
        self.print_info()
        

    @property
    def bead_xy(self):
        # 获取 tk_bead 的位置
        x1, y1, x2, y2 = self.tk_canvas.coords(self.tk_bead)
        return (x1 + x2) / 2, (y1 + y2) / 2
    
    @property
    def bead_size(self):
        # 获取 tk_bead 的大小
        x1, y1, x2, y2 = self.tk_canvas.coords(self.tk_bead)
        print(f"bead size: {(x2 - x1) / 2}")
        return (x2 - x1) / 2
    
    @property
    def label_xy(self):
        return self.tk_canvas.coords(self.label)
        
    
    def set_bead(self, xy, size):
        x, y = xy
        r = size
        # 设置 tk_bead 的位置和大小
        self.tk_canvas.coords(self.tk_bead, 
                              x - r, 
                              y - r, 
                              x + r, 
                              y + r)
    
    def set_label(self, xy, text):
        x, y = xy
        self.tk_canvas.coords(self.label, x, y)
        self.tk_canvas.itemconfig(self.label, text=text)

    def calibrate(self, current_dist, current_mil):
        # TODO 
        # 实现调用接口
        # 
        dy = self.bead_xy[1] - self.tk_center[1]
        pixel_per_mil = dy / current_mil
        dist_per_mil = current_dist / current_mil
        self.accessory.set_pixel_per_mil(pixel_per_mil)
        self.accessory.set_dist_per_mil(dist_per_mil)

    def choose_accessory(self):
        # TODO
        # 实现调用接口
        #
        pass
    
    def print_info(self):
        output = \
f"""
accessory:\t\t\t {self.accessory}
dist_per_mil:\t\t\t {self.accessory.dist_per_mil} m/mil
pixel_per_mil:\t\t\t {self.accessory.pixel_per_mil} pixel/mil
bead_xy:\t\t\t {self.bead_xy} pixel
bead_size:\t\t\t {self.bead_size} pixel
label_xy:\t\t\t {self.label_xy} pixel
current_dist:\t\t\t {self.current_dist} m
current_mil:\t\t\t {self.current_dist / self.accessory.dist_per_mil} mil
current_correcting:\t\t {self.accessory.calculate_correcting(self.current_dist)} pixel
"""
        print(output)


