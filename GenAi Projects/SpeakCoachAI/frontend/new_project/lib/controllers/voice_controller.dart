import 'package:get/get.dart';
import '../services/speech_service.dart';

class VoiceController extends GetxController {
  final SpeechService _speechService = SpeechService();

  var isListening = false.obs;
  var recognizedText = "".obs;

  Future<void> startListening() async {
    isListening.value = true;
    recognizedText.value = await _speechService.listen();
    isListening.value = false;
  }

  Future<void> speakText(String text) async {
    await _speechService.speak(text);
  }
}
