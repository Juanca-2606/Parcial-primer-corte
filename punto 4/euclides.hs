import Data.Time (getCurrentTime, diffUTCTime)

mcd :: Int -> Int -> Int
mcd a 0 = a
mcd a b = mcd b (a `mod` b)

main :: IO ()
main = do
    let a = 1071
    let b = 462
    
    inicio <- getCurrentTime
    
    let resultado = mcd a b
    putStrLn $ "Resultado en Haskell: " ++ show resultado
    
    fin <- getCurrentTime
    putStrLn $ "Tiempo de ejecucion: " ++ show (diffUTCTime fin inicio)