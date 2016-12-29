
let fibonacci number =
  let rec aux n1 n2 = function
    | 0 -> n1
    | n -> aux n2 (n1+n2) (n-1)
  in
  aux 0 1 number

let () =
  let number = read_int() in
  let fibonacci_number = fibonacci number in
  print_int fibonacci_number;;