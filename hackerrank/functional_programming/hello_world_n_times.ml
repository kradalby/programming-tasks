let rec print_hello number =
  match number with
  | 0 -> ()
  | n -> print_string "Hello World\n"; print_hello (number-1)

let () =
  let number = read_int() in
  print_hello number
