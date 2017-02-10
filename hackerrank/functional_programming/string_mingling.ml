#load "str.cma";;

let mingle string1 string2 = 
  let reg = Str.regexp "" in
  List.map2 (fun x y -> x ^ y) (Str.split reg string1) (Str.split reg string2)

let () =
  let string1 = read_line() in
  let string2 = read_line() in
  let answer = mingle string1 string2 in
  print_endline (String.concat "" answer)
