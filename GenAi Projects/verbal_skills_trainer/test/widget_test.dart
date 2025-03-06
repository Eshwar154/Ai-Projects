// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in the test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:get/get.dart';
import 'package:verbal_skills_trainer/main.dart';
import 'package:verbal_skills_trainer/screens/assessment_screen.dart';

void main() {
  testWidgets('Assessment Screen Test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(GetMaterialApp(
      home: AssessmentScreen(),
    ));

    // Verify that the assessment screen shows
    expect(find.text('Presentation Assessment'), findsOneWidget);
    expect(find.text('Submit Your Presentation:'), findsOneWidget);

    // Verify that the upload button exists
    expect(find.text('Upload Audio'), findsOneWidget);

    // Verify that the submit button exists
    expect(find.text('Submit for Evaluation'), findsOneWidget);

    // Verify initial state - no feedback
    expect(find.text('No file selected'), findsOneWidget);
  });
}
