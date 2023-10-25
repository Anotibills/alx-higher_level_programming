#!/usr/bin/node
// A script that computes the numbers of tasks completed
const request = require('request');
const url = process.argv[2];
const tasks = {};

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const taskData = JSON.parse(body);
    for (let i = 0; i < taskData.length; i++) {
      const task = taskData[i];
      const user = task.userId;

      if (task.completed === true) {
        if (user in tasks) {
          tasks[user]++;
        } else {
          tasks[user] = 1;
        }
      }
    }
  } else {
    console.error(error);
  }
  console.log(tasks);
});
