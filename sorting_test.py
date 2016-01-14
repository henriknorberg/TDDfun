import unittest
import sort_animal_action

class SortAnimalTest(unittest.TestCase): 
     
     def test_sort_returns_array(self):
     	
     	 result = sort_animal_action.sort_animal(['cat','fish','dog'])
     	 self.assertEqual(len(result) ,3) 


     def test__returns_sorted_animals(self):

         result = sort_animal_action.sort_animal(['cat','fish','dog'])
     	 self.assertTrue(result, ['cat','dog','fish'])


     def test__returns_dog_false_shouldbetrue(self):

         result = sort_animal_action.sort_animal(['dog','dog'])
     	 self.assertFalse(result, ['dog','dog'])


     def test_reverted_sort(self):

         result = sort_animal_action.sort_animal(['dog','fish','cat'])
         self.assertTrue(result, ['dog', 'fish', 'cat'])


     def test_list_is_a_list(self):     
        
         result = sort_animal_action.sort_animal(['dog','fish','cat'])
         self.assertIsInstance(result, list)




