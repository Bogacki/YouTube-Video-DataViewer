from tkinter import *
from tkinter.ttk import *
from youtube import *
from functools import partial

class UI(Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Videos Data Viewer")
        self.geometry('600x500')
        self.search_video_input = Entry(width=40)
        self.search_video_input.place(relx=0.5,y=50, anchor=CENTER)
        self.print_subscribers_btn = Button(self,text="Search", width=30, command=self.show_videos).place(relx=0.5,y=80,anchor=CENTER)
        self.youtube = yt()
        self.mainloop()



    def show_videos(self):
        videos = self.youtube.search_videos(self.search_video_input.get())
        for index, video in enumerate(videos):
            Button(self,text=f"{index+1}. {video.text[0:75]}",command= partial(self.show_video_data,index)).place(relx=0.5,y=130+index*35, anchor=CENTER, width=400)


    def show_video_data(self,index):
        video_data = self.youtube.get_video_data(index)
        Label(text=f"Title:{video_data.title}").place(relx=0.5,y=300, anchor=CENTER, width=400)
        Label(text=f"Author:{video_data.author}").place(relx=0.5,y=320, anchor=CENTER, width=400)
        Label(text=f"Length:{round(video_data.length / 60)} minutes").place(relx=0.5,y=340, anchor=CENTER, width=400)
        Label(text=f"Publication date:{video_data.publish_date}").place(relx=0.5,y=360, anchor=CENTER, width=400)
        Label(text=f"Link:{video_data.watch_url}").place(relx=0.5,y=380, anchor=CENTER, width=400)




