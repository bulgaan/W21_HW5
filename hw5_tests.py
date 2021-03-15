#########################################
##### Name: Bulgan Jugderkhuu       #####
##### Uniqname: bulgan              #####
#########################################

import unittest
import hw5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q1 = hw5_cards.Card(rank=12)
        self.assertEqual(q1.rank_name, "Queen")
        return q1.rank_name, "Queen"
    
    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        s1 = hw5_cards.Card(suit=1)
        self.assertEqual(s1.suit_name, "Clubs")
        return s1.suit_name, "Clubs"
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c3 = hw5_cards.Card(suit=3,rank=13)
        x = c3.__str__()
        self.assertEqual(x, "King of Spades")
        return x, "King of Spades"
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a Deck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        d1 = hw5_cards.Deck()
        d1_len = len(d1.cards)
        self.assertEqual(d1_len, 52)
        return d1_len, 52


    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        d2 = hw5_cards.Deck()
        x = d2.deal_card()
        self.assertTrue(isinstance(x,hw5_cards.Card))
        return x, hw5_cards.Card
        
        
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        d3 = hw5_cards.Deck()
        d3_len = len(d3.cards)
        d3.deal_card()
        d3_new = len(d3.cards)
        self.assertEqual(d3_len-1, d3_new)
        return d3_len-1, d3_new
    
    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        d5 = hw5_cards.Deck()
        prev_len = len(d5.cards)
        card = d5.deal_card()
        mid_len = len(d5.cards)
        d5.replace_card(card)
        new_len = len(d5.cards)
        self.assertEqual(prev_len,mid_len+1, new_len)
        return prev_len, mid_len+1, new_len

    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        d6 = hw5_cards.Deck()
        old_len = len(d6.cards)
        card = d6.deal_card()
        d6.replace_card(card) #this returns it to the original
        mid_len = len(d6.cards)
        d6.replace_card(card)
        new_len = len(d6.cards)
        self.assertEqual(mid_len,new_len)
        return mid_len, new_len



if __name__=="__main__":
    unittest.main()