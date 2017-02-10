#load "str.cma";;

let rec read_lines () =
  try let line = read_line () in
    line :: read_lines()
  with
    End_of_file -> []

let permute str =
  let rec aux acc = function
    | [] -> acc
    | l -> 
      let h = List.hd l in
      let t = List.tl l in
      let h2 = List.hd t in
      let t2 = List.tl t in
      aux (acc@[h2; h]) t2
  in
  aux [] str;;

let permute2 str =
  let rec aux acc = function
    | [] -> acc
    | h::(h2::t) -> 
      aux (acc@[h2; h]) t
  in
  aux [] str;;

let f strings =
  let rec aux acc = function
    | [] -> acc
    | h::t -> 
      aux (acc@[permute2 (Str.split (Str.regexp "") h)]) t
  in
  aux [] strings;;


let () = 
  let _ = read_int() in
  let arr = read_lines() in
  let ans = f arr in
  List.iter (fun string_array -> (print_endline (String.concat "" string_array))) ans;;