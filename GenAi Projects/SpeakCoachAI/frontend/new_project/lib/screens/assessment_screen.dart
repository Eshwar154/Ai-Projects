import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/assessment_controller.dart';

class AssessmentScreen extends StatelessWidget {
  final AssessmentController controller = Get.put(AssessmentController());

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Presentation Assessment"),
      ),
      body: Padding(
        padding: EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text("Submit Your Presentation:",
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            SizedBox(height: 10),
            TextField(
              controller: controller.textController,
              maxLines: 5,
              decoration: InputDecoration(
                hintText: "Paste or type your presentation script here...",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton.icon(
              onPressed: controller.pickAudioFile,
              icon: Icon(Icons.audiotrack),
              label: Text("Upload Audio"),
            ),
            SizedBox(height: 10),
            Obx(() => Text(controller.audioFilePath.value.isNotEmpty
                ? "Selected: ${controller.audioFilePath.value.split('/').last}"
                : "No file selected")),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: controller.submitAssessment,
              child: Text("Submit for Evaluation"),
            ),
            SizedBox(height: 20),
            Obx(() => controller.feedback.value.isNotEmpty
                ? Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text("Feedback:",
                          style: TextStyle(
                              fontSize: 18, fontWeight: FontWeight.bold)),
                      SizedBox(height: 10),
                      Text(controller.feedback.value),
                    ],
                  )
                : SizedBox()),
          ],
        ),
      ),
    );
  }
}
