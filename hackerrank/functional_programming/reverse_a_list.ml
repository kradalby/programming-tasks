let rec read_lines () =
  try let line = read_line () in
    int_of_string (line) :: read_lines()
  with
    End_of_file -> []

let rec reverse lst acc =
  match lst with 
  | [] -> acc
  | head::tail -> reverse tail (head::acc)

let f lst = 
  reverse lst [];;

let () = 
  let arr = read_lines() in
  let ans = f arr in
  List.iter (fun x -> print_int x; print_newline ()) ans;;