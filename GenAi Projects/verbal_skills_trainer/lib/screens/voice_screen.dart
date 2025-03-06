import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/voice_controller.dart';

class VoiceScreen extends StatelessWidget {
  final VoiceController voiceController = Get.put(VoiceController());

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Voice Interaction")),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Obx(() => Text(
                voiceController.recognizedText.value.isEmpty
                    ? "Press the mic and start speaking..."
                    : voiceController.recognizedText.value,
                style: TextStyle(fontSize: 20),
              )),
          SizedBox(height: 20),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              FloatingActionButton(
                onPressed: () => voiceController.startListening(),
                child: Icon(Icons.mic),
              ),
              SizedBox(width: 20),
              FloatingActionButton(
                onPressed: () => voiceController.speakText(
                    voiceController.recognizedText.value),
                child: Icon(Icons.volume_up),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
