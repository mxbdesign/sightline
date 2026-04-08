from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # use evaluate canvas to bypass fonts timeout as instructed in memory
        page.goto('http://localhost:8000/v3.html', wait_until='load')
        page.wait_for_timeout(2000) # Wait for animation to draw something

        # screenshot for visual verification
        page.screenshot(path='/home/jules/verification/base_play.png')

        # set game state to quiz
        page.evaluate("gameState = 'QUIZ'; activeNPC = npcs[0];")
        page.wait_for_timeout(500)
        page.screenshot(path='/home/jules/verification/quiz.png')

        browser.close()

if __name__ == '__main__':
    test()
