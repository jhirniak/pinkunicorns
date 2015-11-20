angular.module('todoApp', [])
  .controller('TodoListController', function() {
    var todoList = this;
    todoList.todos = [
      {text:'learn angular', done:true},
      {text:'build an angular app', done:false}];
 
    todoList.addTodo = function() {
      todoList.todos.push({text:todoList.todoText, done:false});
      todoList.todoText = '';
    };
  }).controller('ModalController', function() {
    var modal = this;
    modal.text = "Some text";
    modal.event = {};
    modal.events = [];

    modal.setEvents = function(events) {
      modal.events = events;
    }

    modal.setEvent = function(eid) {
      for(var i = 0; i < modal.events.length; i++) {
        alert(modal.events[i].id);
      }
      modal.event = modal.events[eid];
    };
  });