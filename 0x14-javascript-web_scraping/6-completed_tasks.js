#!/usr/bin/node
//A script that computes the numbers of tasks completed
const request = require('request');
let url = process.argv[2];
let tasks = {};

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const taskData = JSON.parse(body);
    for (let i = 0; i < taskData.length; i++) {
      let task = taskData[i];
      let user = task.userId;

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
