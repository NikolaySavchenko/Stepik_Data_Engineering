
//### Что было изменено:
//  1. **Удаление изменяемых переменных**: Убрали изменяемую переменную result.
//2. **Использование методов высшего порядка**: Заменили цикл for для перебора списка и
// условие на методы filter и map.
//- filter(_.length > 3) выбирает только те строки, длина которых превышает 3 символа.
//- map(_.toUpperCase) преобразует строки в верхний регистр.
//3. **Код стал более декларативным**, демонстрируя, что мы хотим сделать (фильтрация и преобразование),
// а не как это сделать (используя циклы и изменяемые переменные).

object StringProcessor {
  // Преобразовали метод processStrings, используя filter и map вместо изменяемых переменных и циклов.
  def processStrings(strings: List[String]): List[String] = {
    // Отбираем только те строки, длина которых больше 3, и преобразуем их в верхний регистр
    val result = strings.filter(_.length > 3).map(_.toUpperCase)
    result
  }

  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
  }
}
