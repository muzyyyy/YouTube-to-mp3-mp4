from pytube import YouTube
import os

link = input('PLEASE PUT A VALID YOUTUBE LINK: ')
yt = YouTube(link)


question = input('Do you want VIDEO or AUDIO?(v/a)') #Ask if user wants to download video or audio

if question.lower().startswith("v"):#video download
        while True:

            print("Title: ", yt.title) #print youtube title
            answer = input('Is this the title?(y/n):') #Ask if given info is correct

            if answer.lower().startswith("y"): #if yes then download video 
                print('DOWNLOADING')
                yd = yt.streams.get_highest_resolution()
                print("Enter the destination or leave blank for current directory")
                destination = str(input(">> ")) or '.'

                # download the file
                out_file = yd.download(output_path=destination)
  
                # save the file
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)

                print('Succesfully Downloaded ', yt.title)

            elif answer.lower().startswith("n"): #if no terminate code
                print("ok, Terminating")
                exit()

