import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'chat_screen.dart';
import 'voice_screen.dart';
import 'assessment_screen.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("AI Verbal Trainer"),
        centerTitle: true,
      ),
      body: Padding(
        padding: EdgeInsets.all(20),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            HomeButton(
              title: "Chat Training",
              icon: Icons.chat,
              onPressed: () => Get.to(() => ChatScreen()),
            ),
            SizedBox(height: 20),
            HomeButton(
              title: "Voice Training",
              icon: Icons.mic,
              onPressed: () => Get.to(() => VoiceScreen()),
            ),
            SizedBox(height: 20),
            HomeButton(
              title: "Presentation Assessment",
              icon: Icons.assignment,
              onPressed: () => Get.to(() => AssessmentScreen()),
            ),
          ],
        ),
      ),
    );
  }
}

class HomeButton extends StatelessWidget {
  final String title;
  final IconData icon;
  final VoidCallback onPressed;

  HomeButton({required this.title, required this.icon, required this.onPressed});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: onPressed,
      style: ElevatedButton.styleFrom(
        padding: EdgeInsets.symmetric(vertical: 15, horizontal: 30),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, size: 24),
          SizedBox(width: 10),
          Text(title, style: TextStyle(fontSize: 18)),
        ],
      ),
    );
  }
}
