from RealtimeSTT import AudioToTextRecorder
import assist_deepseek
import time
import tools_deepseek


if __name__ == '__main__':
    recorder = AudioToTextRecorder(spinner=False, model="tiny.en", language="en", post_speech_silence_duration =0.1, silero_sensitivity = 0.4)
    hot_words = ["hey"]
    #skip_hot_word_check = False
    skip_hot_word_check = True
    print("Say something...")
    while True:
        current_text = recorder.text()
        print(current_text)
        if any(hot_word in current_text.lower() for hot_word in hot_words) or skip_hot_word_check:
                    if current_text:
                        print("User: " + current_text)
                        recorder.stop()
                        current_text = current_text + " " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                        response = assist_deepseek.ask_question_memory(current_text)
                        print(response)
                        speech = response.split('#')[0]
                        done = assist_deepseek.TTS(speech)
                        skip_hot_word_check = True if "?" in response else False
                        #if len(response.split('#')) > 1:
                        #    command = response.split('#')[1]
                        #    tools_deepseek.parse_command(command)
                        #recorder.start()