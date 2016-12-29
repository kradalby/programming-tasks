

let compare a b = 


  let () =
    let alice = List.map int_of_string (Str.split (Str.regexp " ") (read_line())) in
    let bob = List.map int_of_string (Str.split (Str.regexp " ") (read_line())) in
    let result = List.fold_left2 compare alice bob in