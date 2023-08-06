from .utils.audio_source import AudioStream
from .service.streaming_recognizer import StreamingRecognizer


class TechmoSettings(dict):
    def __getattr__(self, key):
        try:
            return lambda: self[key]
        except KeyError as k:
            raise AttributeError(k)


def transcribe_with_techmo(
    wave_path,
    techmo_address,
    techmo_ssl_dir="",
    grpc_timeout=0,
    interim_results=False,
    max_alternatives=1,
    no_input_timeout=5000,
    recognition_timeout=1000,
    single_utterance=False,
    speech_complete_timeout=2000,
    speech_incomplete_timeout=4000,
    time_offsets=False,
):

    settings = TechmoSettings(
        context_phrase="",
        grpc_timeout=grpc_timeout,
        interim_results=interim_results,
        max_alternatives=max_alternatives,
        mic=None,
        session_id=None,
        single_utterance=single_utterance,
        timeouts_map={
            "no-input-timeout": str(no_input_timeout),
            "speech-complete-timeout": str(speech_complete_timeout),
            "speech-incomplete-timeout": str(speech_incomplete_timeout),
            "recognition-timeout": str(recognition_timeout),
        },
        time_offsets=time_offsets,
        wave_path=wave_path,
    )

    with AudioStream(wave_path) as stream:
        recognizer = StreamingRecognizer(techmo_address, techmo_ssl_dir, settings)
        results = recognizer.recognize(stream)

    return results
