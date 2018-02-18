import Foundation


var T = Int(readLine()!)


if let T = T{
 for num in 1..<T+1 {
    let a = readLine()

    if let a = a{
    var array = a.components(separatedBy: " ")

    var sum = Int(array[0])! + Int(array[1])!
    
        print("Case #\(num): \(sum)")
    }
    }
}
