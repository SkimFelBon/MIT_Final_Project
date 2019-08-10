$( function() {
  $("#basicDate").flatpickr({
      enableTime: true,
      dateFormat: "F, d Y H:i"
  });

  $("#rangeDate").flatpickr({
      mode: 'range',
      closeOnSelect: false,
      dateFormat: "Y-m-d"
  });

  $("#timePickerFrom").flatpickr({
      enableTime: true,
      noCalendar: true,
      time_24hr: true,
      dateFormat: "H:i",
  });

  $("#timePicker").flatpickr({
      enableTime: true,
      noCalendar: true,
      time_24hr: true,
      dateFormat: "H:i",
  });

  $(".resetDate").flatpickr({
      wrap: false,
  });
} );
