isPrime :: Int -> Bool
isPrime num
    | num <= 1 = False
    | otherwise = all (\x -> num `mod` x /= 0) [2..(floor . sqrt $ fromIntegral num)]

main :: IO ()
main = do
    putStrLn "Enter a number: "
    n <- readLn
    putStrLn $ "Prime numbers up to " ++ show n ++ " are:"
    mapM_ (\x -> if isPrime x then putStr (show x ++ " ") else return ()) [2..n]
