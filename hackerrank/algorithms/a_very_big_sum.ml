#load "str.cma";;

let rec sum l = 
  match l with
  | [] -> Int64.zero
  | h::t -> Int64.add h (sum t);;

let () = 
  let length = read_int() in
  let input = read_line() in
  let input_as_list = (Str.split (Str.regexp " ") input) in 
  print_string (Int64.to_string (sum (List.map Int64.of_string input_as_list)))
