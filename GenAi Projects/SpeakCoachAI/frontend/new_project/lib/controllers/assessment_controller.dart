import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:file_picker/file_picker.dart';

class AssessmentController extends GetxController {
  TextEditingController textController = TextEditingController();
  RxString audioFilePath = ''.obs;
  RxString feedback = ''.obs;

  void pickAudioFile() async {
    FilePickerResult? result =
        await FilePicker.platform.pickFiles(type: FileType.audio);
    if (result != null) {
      audioFilePath.value = result.files.single.path!;
    }
  }

  void submitAssessment() {
    if (textController.text.isEmpty && audioFilePath.value.isEmpty) {
      Get.snackbar(
          "Error", "Please submit either text or audio for assessment");
      return;
    }

    // TODO: Implement API call to FastAPI backend
    feedback.value = "Your assessment feedback will be displayed here.";
  }

  @override
  void onClose() {
    textController.dispose();
    super.onClose();
  }
}
