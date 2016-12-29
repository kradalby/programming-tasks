

let rec gcd x y =
  if x == y then
    x
  else if x > y then
    gcd (x-y) y
  else 
    gcd x (y-x)



let rec read_lines () = 
  try let line = read_line () in
    line :: read_lines()
  with
    End_of_file -> []



let () =
  let inp = read_line() in
  let arr = List.map int_of_string (Str.split (Str.regexp " ") inp) in
  let x = List.nth arr 0 in
  let y = List.nth arr 1 in
  let answer = gcd x y in
  print_int answer;;