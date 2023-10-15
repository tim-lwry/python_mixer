from pydub import AudioSegment
import os
import traceback

# ffmpeg and ffprobe required

class Mixer:
    module_path = os.path.dirname(os.path.abspath(__file__))+"\\"
    @staticmethod
    def combine2(f1, f2, f="mp3"):
        try:
            #print(os.path.isfile(Mixer.module_path+f1))
            sound1 = AudioSegment.from_file(Mixer.module_path+f1)
            sound2 = AudioSegment.from_file(Mixer.module_path+f2)
            
            output = sound1+sound2
            
            out_ = output.export(f1+"_and_"+f2+"_combined."+f, format=f)
            out_.close()
            return True
        except Exception as error:
            print("An exception occurred:", error)
            traceback.print_exc()
            return False

    @staticmethod
    def overlay2(f1, f2, t=0, f="mp3"):
        try:
            if t<0:
                raise Exception("Negative offset")
            #print(os.path.isfile(Mixer.module_path+f1))
            sound1 = AudioSegment.from_file(Mixer.module_path+f1)
            sound2 = AudioSegment.from_file(Mixer.module_path+f2)
            
            output = sound1.overlay(sound2, t)
            
            out_ = output.export(f1+"_and_"+f2+"_overlayed."+f, format=f)
            out_.close()
            return True
        except Exception as error:
            print("An exception occurred:", error)
            traceback.print_exc()
            return False

    @staticmethod
    def mix2(f1, f2, s1, s2, offset=0, f="mp3", e1=None, e2=None):
        try:
            sound1 = AudioSegment.from_file(Mixer.module_path+f1)
            sound2 = AudioSegment.from_file(Mixer.module_path+f2)

            if e1 == None:
                e1 = len(sound1)
            if e2 == None:
                e2 = len(sound2)

            if offset<0 or s1<0 or s2<0 or e1<0 or e2<0:
                raise Exception("Negative offset")

            segment1 = sound1[s1: e1]
            segment2 = sound2[s2: e2]

            output = segment1.overlay(segment2, offset)
            
            out_ = output.export(f1+"_and_"+f2+"_mixed."+f, format=f)
            out_.close()
            return True
        except Exception as error:
            print("An exception occurred:", error)
            traceback.print_exc()
            return False

