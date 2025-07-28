import pygame
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.board import init_board, make_move
from game.rules import get_winner, is_valid_move
from ai.minimax_ai import minimax_ai

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
LINE_WIDTH = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class TicTacToeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 100))
        pygame.display.set_caption("Tic Tac Toe - Human vs AI")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        
        # Game state
        self.board = init_board()
        self.human_player = 'X'
        self.ai_player = 'O'
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        
    def draw_grid(self):
        """Draw the tic-tac-toe grid"""
        # Horizontal lines
        for i in range(1, GRID_SIZE):
            pygame.draw.line(self.screen, BLACK, 
                           (0, i * CELL_SIZE), 
                           (WINDOW_SIZE, i * CELL_SIZE), LINE_WIDTH)
        
        # Vertical lines
        for i in range(1, GRID_SIZE):
            pygame.draw.line(self.screen, BLACK, 
                           (i * CELL_SIZE, 0), 
                           (i * CELL_SIZE, WINDOW_SIZE), LINE_WIDTH)
    
    def draw_marks(self):
        """Draw X's and O's"""
        for row in range(3):
            for col in range(3):
                if self.board[row][col] != '_':
                    x = col * CELL_SIZE + CELL_SIZE // 2
                    y = row * CELL_SIZE + CELL_SIZE // 2
                    
                    text = self.font.render(self.board[row][col], True, 
                                          BLUE if self.board[row][col] == 'X' else RED)
                    text_rect = text.get_rect(center=(x, y))
                    self.screen.blit(text, text_rect)
    
    def draw_status(self):
        """Draw game status"""
        if self.game_over:
            if self.winner == self.human_player:
                status = "You Won! Press R to restart"
                color = GREEN
            elif self.winner == self.ai_player:
                status = "AI Won! Press R to restart"
                color = RED
            else:
                status = "Draw! Press R to restart"
                color = BLACK
        else:
            if self.current_player == self.human_player:
                status = "Your turn - Click a square"
                color = BLUE
            else:
                status = "AI is thinking..."
                color = RED
        
        text = self.small_font.render(status, True, color)
        text_rect = text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE + 50))
        self.screen.blit(text, text_rect)
    
    def handle_click(self, pos):
        """Handle mouse click"""
        if self.game_over or self.current_player != self.human_player:
            return
        
        col = pos[0] // CELL_SIZE
        row = pos[1] // CELL_SIZE
        
        if row < 3 and col < 3 and is_valid_move(self.board, (row, col)):
            self.board = make_move(self.board, (row, col), self.human_player)
            
            if not self.check_game_end():
                self.current_player = self.ai_player
    
    def make_ai_move(self):
        """Make AI move"""
        if self.game_over or self.current_player != self.ai_player:
            return
        
        ai_move = minimax_ai(self.board, self.ai_player)
        if ai_move:
            self.board = make_move(self.board, ai_move, self.ai_player)
            
            if not self.check_game_end():
                self.current_player = self.human_player
    
    def check_game_end(self):
        """Check if game has ended"""
        winner = get_winner(self.board)
        
        if winner != '_':
            self.game_over = True
            self.winner = winner
            return True
        
        # Check for draw
        if all(self.board[i][j] != '_' for i in range(3) for j in range(3)):
            self.game_over = True
            self.winner = None
            return True
        
        return False
    
    def restart_game(self):
        """Restart the game"""
        self.board = init_board()
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
    
    def run(self):
        """Main game loop"""
        running = True
        ai_move_timer = 0
        
        while running:
            dt = self.clock.tick(60)
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart_game()
            
            # AI move with delay
            if self.current_player == self.ai_player and not self.game_over:
                ai_move_timer += dt
                if ai_move_timer > 1000:  # 1 second delay
                    self.make_ai_move()
                    ai_move_timer = 0
            
            # Draw everything
            self.screen.fill(WHITE)
            self.draw_grid()
            self.draw_marks()
            self.draw_status()
            
            pygame.display.flip()
        
        pygame.quit()

def main():
    """Run the Pygame version"""
    game = TicTacToeGame()
    game.run()

if __name__ == "__main__":
    main()