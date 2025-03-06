import 'package:get/get.dart';
import '../services/api_service.dart';

class ChatController extends GetxController {
  var messages = <Map<String, String>>[].obs;
  var isLoading = false.obs;

  void sendMessage(String userMessage) async {
    messages.add({"role": "user", "text": userMessage});
    isLoading.value = true;

    String botResponse = await ApiService.chatWithAI(userMessage);
    messages.add({"role": "bot", "text": botResponse});

    isLoading.value = false;
  }
}
