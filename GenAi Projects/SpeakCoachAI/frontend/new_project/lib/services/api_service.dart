import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  static const String baseUrl =
      "http://localhost:8000"; // Replace with actual server URL

  static Future<String> chatWithAI(String message) async {
    final response = await http.post(
      Uri.parse("$baseUrl/chat"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"text": message}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body)["response"];
    } else {
      return "Error: Could not get response.";
    }
  }

  static Future<List<String>> getTrainingModules() async {
    // TODO: Replace with actual API call
    return [
      'Public Speaking Basics',
      'Voice Modulation',
      'Body Language',
      'Presentation Skills'
    ];
  }
}
