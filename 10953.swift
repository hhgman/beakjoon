import Foundation


var T = Int(readLine()!)


if let T = T{
 for num in 0..<T {
    let a = readLine()

    if let a = a{
    var array = a.components(separatedBy: ",")

    print(Int(array[0])! + Int(array[1])!)
    }
    }
}
