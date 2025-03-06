import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../services/api_service.dart';

class TrainingScreen extends StatefulWidget {
  @override
  _TrainingScreenState createState() => _TrainingScreenState();
}

class _TrainingScreenState extends State<TrainingScreen> {
  List<String> trainingModules = [];

  @override
  void initState() {
    super.initState();
    fetchTrainingModules();
  }

  Future<void> fetchTrainingModules() async {
    try {
      var response = await ApiService.getTrainingModules();
      setState(() {
        trainingModules = response;
      });
    } catch (e) {
      print("Error fetching training modules: $e");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Training Modules")),
      body: trainingModules.isEmpty
          ? Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: trainingModules.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(trainingModules[index]),
                  trailing: Icon(Icons.play_arrow),
                  onTap: () {
                    Get.to(() => TrainingDetailScreen(module: trainingModules[index]));
                  },
                );
              },
            ),
    );
  }
}

class TrainingDetailScreen extends StatelessWidget {
  final String module;

  TrainingDetailScreen({required this.module});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(module)),
      body: Center(
        child: Text("Training content for $module"),
      ),
    );
  }
}
