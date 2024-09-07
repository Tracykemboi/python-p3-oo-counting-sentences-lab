#!/usr/bin/env python3

class MyString:
  def __init__(self,value=''):
    self.value = value
  
  @property 
  def value(self):
    return self._value
  
  @value.setter
  def value(self,value):
     if isinstance(value,str):
      self._value = value
     else:
       print('The value must be a string.')
  def is_sentence(self):
    return self._value.strip().endswith('.')
  def is_question(self):
    return self._value.strip().endswith('?')
  def is_exclamation(self):
    return self._value.strip().endswith('!')
  def count_sentences(self):
        # First, replace '...' with a placeholder
        temp = self._value.replace('...', '<ELLIPSIS>')
        # Then replace '!' and '?' with '.'
        modified_value = temp.replace('!', '.').replace('?', '.')
        # Finally, replace the placeholder with a single '.'
        final_value = modified_value.replace('<ELLIPSIS>', '.')
        # Count the periods, but don't count empty sentences
        return sum(1 for s in final_value.split('.') if s.strip())
    


