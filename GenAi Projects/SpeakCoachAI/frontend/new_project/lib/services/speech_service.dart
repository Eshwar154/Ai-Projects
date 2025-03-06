import 'package:speech_to_text/speech_to_text.dart' as stt;
import 'package:flutter_tts/flutter_tts.dart';

class SpeechService {
  final stt.SpeechToText _speech = stt.SpeechToText();
  final FlutterTts _tts = FlutterTts();

  Future<String> listen() async {
    bool available = await _speech.initialize();
    if (available) {
      _speech.listen();
      return _speech.lastRecognizedWords;
    } else {
      return "Speech recognition not available.";
    }
  }

  Future<void> speak(String text) async {
    await _tts.speak(text);
  }
}
