document.addEventListener('DOMContentLoaded', function () {
    // Select the relevant DOM elements
    const addItem = document.getElementById('add_item');
    const removeItem = document.getElementById('remove_item');
    const clearList = document.getElementById('clear_list');
    const myList = document.querySelector('.my_list');
  
    // Function to add a new item to the list
    addItem.addEventListener('click', function () {
      const newItem = document.createElement('li');
      newItem.textContent = 'Item';
      myList.appendChild(newItem);
    });
  
    // Function to remove the last item from the list
    removeItem.addEventListener('click', function () {
      const lastItem = myList.lastElementChild;
      if (lastItem) {
        myList.removeChild(lastItem);
      }
    });
  
    // Function to clear all items from the list
    clearList.addEventListener('click', function () {
      while (myList.firstChild) {
        myList.removeChild(myList.firstChild);
      }
    });
  });
  