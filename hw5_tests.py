######################################### 
# ##### Name: Yue wang ##### 
# ##### Uniqname:wyjessic ##### 
# #########################################
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
        card1 = hw5_cards.Card(0,12)
        self.assertEqual(card1.rank_name,"Queen")
        return card1.rank_name, "Queen"
    
    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        card2 = hw5_cards.Card(1,12)
        self.assertEqual(card2.suit_name,"Clubs")
        return card2.suit_name,"Clubs"
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is 
        created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. 
        # But returning will allow for unit testing of your unit test, 
        # and allow you to check your answer with the autograder.  This is optional today.

        '''
        card3 = hw5_cards.Card(3,13)
        self.assertEqual(card3.__str__(),"King of Spades")
        return card3.__str__(),"King of Spades"
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, 
        it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck4 = hw5_cards.Deck()
        self.assertEqual(len(deck4.cards),52)
        return len(deck4.cards),52

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, 
        it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck5 = hw5_cards.Deck()
        self.assertIsInstance(deck5.deal_card(), hw5_cards.Card)
        return deck5.deal_card(), hw5_cards.Card
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, 
        the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck6 = hw5_cards.Deck()
        lengh_deck6 = len(deck6.cards)
        deck6.deal_card()
        lengh_deck6_deal = len(deck6.cards)
        self.assertEqual(
            lengh_deck6-1,  lengh_deck6_deal
        )
        return   lengh_deck6-1,  lengh_deck6_deal  
    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method,
        the deck has one more card in it afterwards.
         (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck7 = hw5_cards.Deck()
        lengh_deck7 = len(deck7.cards)
        card = deck7.deal_card()
        lengh_deck7_deal = len(deck7.cards)
        deck7.replace_card(card)
        lengh_deck7_replace = len(deck7.cards)
        self.assertEqual(
            lengh_deck7, lengh_deck7_deal+1, lengh_deck7_replace
        )
        return   lengh_deck7, lengh_deck7_deal+1, lengh_deck7_replace


        
    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, 
        the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        deck8 = hw5_cards.Deck()
        card = deck8.deal_card()
        deck8.replace_card(card)
        lengh_deck8 = len(deck8.cards)
        # we already know that card is in the deck8, we replace it twice
        deck8.replace_card(card)
        lengh_deck8_du_replace = len(deck8.cards)

        self.assertEqual(
            lengh_deck8,  lengh_deck8_du_replace
        )
        return   lengh_deck8,  lengh_deck8_du_replace



if __name__=="__main__":
    unittest.main()