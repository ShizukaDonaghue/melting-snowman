def draw_snowman(number_of_lives):
    """
    Draw snowman based on the number of lives left.
    """
    if number_of_lives == 10:
        print("*   *    *    *    *    *    *    *    *    *    *    *    *")
        print("  *    *    *    *    *    *    *    *    *    *    *    *  ")
        print("*    *     *    *     *     *     *      *     *     *     *")
        print("  *     *     *    *     *     *     *     *     *     *    ")
        print("*    *   ___███████___     *      *     *     *      *     *")
        print("    *      ▄▀     ▀▄           *     *     *       *    *   ")
        print("*  \\|/    █  ^ < ^  █    \\|/     *    *    *    *     *    *")
        print("     \\     ▀▄▄▄▄▄▄▄▀     /     *     *      *     *     *   ")
        print("*   * \\   ▄▀       ▀▄   /        *      *      *      *    *")
        print("  *    \\▄▀     0     ▀▄/     *     *     *      *     *     ")
        print("*   *   █      0      █        *      *      *      *      *")
        print("   *   * ▀▄    0    ▄▀     *      *      *     *       *    ")
        print("*    *     ▀▄▄▄▄▄▄▄▀     *      *      *      *      *     *")
        print("\n")
    elif number_of_lives == 9:
        print("*        *      *       *       *        *        *        *")
        print("    *         *           *         *        *        *     ")
        print("*          *          *        *          *                *")
        print("   *                    *          *         *        *     ")
        print("*        ___███████___        *          *        *        *")
        print("    *      ▄▀     ▀▄       *                  *        *    ")
        print("*  \\|/    █  ' < '  █    \\|/     *                 *       *")
        print("     \\     ▀▄▄▄▄▄▄▄▀     /            *       *        *    ")
        print("*     \\   ▄▀       ▀▄   /        *        *       *        *")
        print("  *    \\▄▀     0     ▀▄/    *        *        *        *    ")
        print("*       █      0      █          *        *        *       *")
        print("   *     ▀▄    0    ▄▀       *         *              *     ")
        print("*     *    ▀▄▄▄▄▄▄▄▀      *       *        *        *      *")
        print("\n")
    elif number_of_lives == 8:
        print("*        *      *       *       *        *        *        *")
        print("    *         *           *         *             \\|/      ")
        print("*          *          *        *          *     -- O --    *")
        print("   *                    *          *         *    /|\\  *   ")
        print("*        ___███████___        *          *                 *")
        print("    *      ▄▀     ▀▄       *                  *        *    ")
        print("*  \\|/    █  ' < '  █    \\|/     *        *                *")
        print("     \\     ▀▄▄▄▄▄▄▄▀     /            *       *        *    ")
        print("*     \\   ▄▀       ▀▄   /        *        *       *        *")
        print("  *    \\▄▀     0     ▀▄/    *        *        *        *    ")
        print("*       █      0      █          *        *        *       *")
        print("   *     ▀▄    0    ▄▀       *         *              *     ")
        print("*     *    ▀▄▄▄▄▄▄▄▀      *       *        *        *      *")
        print("\n")
    elif number_of_lives == 7:
        print("*        *      *       *       *        *        *        *")
        print("    *         *           *         *             \\|/      ")
        print("*          *          *        *          *     -- O --    *")
        print("   *                    *          *         *    /|\\  *   ")
        print("*        ___███████___        *    ╔════════╗    *         *")
        print("    *      ▄▀     ▀▄       *       ║        ║         *     ")
        print("*  \\|/    █  ' < '  █    \\|/       ║════════╝      *       *")
        print("     \\     ▀▄▄▄▄▄▄▄▀     /         ║         *         *    ")
        print("*     \\   ▄▀       ▀▄   /          ║    *        *         *")
        print("  *    \\▄▀     0     ▀▄/    *      ║         *        *     ")
        print("*       █      0      █            ║    *        *         *")
        print("   *     ▀▄    0    ▄▀       *     ║       *        *       ")
        print("*     *    ▀▄▄▄▄▄▄▄▀      *        ║     *        *        *")
        print("\n")
    elif number_of_lives == 6:
        print("*           *                 *              *             *")
        print("    *                 *             *             \\|/      ")
        print("*          *                 *              *   -- O --    *")
        print("   *                              *               /|\\      ")
        print("*        ___███████___       *     ╔════════╗    *         *")
        print("    *      ▄▀     ▀▄               ║  HELP! ║         *     ")
        print("*  \\|/    █  ; < ;  █    \\|/       ║════════╝              *")
        print("     \\     ▀▄▄▄▄▄▄▄▀     /         ║               *        ")
        print("*     \\   ▄▀       ▀▄   /          ║  *     *              *")
        print("  *    \\▄▀     0     ▀▄/    *      ║             *         ")
        print("*       █      0      █            ║          *            *")
        print("         ▀▄    0    ▄▀       *     ║     *          *       ")
        print("*     *    ▀▄▄▄▄▄▄▄▀      *        ║           *           *")
        print("\n")
    elif number_of_lives == 5:
        print("*           *                 *              *             *")
        print("    *                 *             *             \\|/      ")
        print("*          *                 *              *   -- O --    *")
        print("   *                              *               /|\\      ")
        print("*        ___███████___       *     ╔════════╗    *         *")
        print("    *      ▄▀     ▀▄               ║  HELP! ║         *     ")
        print("*         █  ; _ ;  █     *        ║════════╝              *")
        print("      *    ▀▄▄▄▄▄▄▄▀               ║               *        ")
        print("*    /\\   ▄▀       ▀▄   /\\         ║  *     *              *")
        print("    /  \\▄▀     0     ▀▄/  \\        ║             *         ")
        print("*  /\\   █             █   /\\       ║          *           *")
        print("         ▀▄    0    ▄▀       *     ║     *          *       ")
        print("*     *    ▀▄▄▄▄▄▄▄▀      *        ║           *           *")
        print("\n")
    elif number_of_lives == 4:
        print("*           *                 *              *             *")
        print("    *                 *             *             \\|/      ")
        print("*          *                 *              *   -- O --    *")
        print("   *                              *               /|\\      ")
        print("*          *            *          ╔════════╗    *         *")
        print("    *      ▄▀     ▀▄               ║  HELP! ║         *     ")
        print("*         █  ; _ ;  █     *        ║════════╝              *")
        print("      *    ▀▄▄▄▄▄▄▄▀               ║               *        ")
        print("*    /\\   ▄▀       ▀▄   /\\         ║        *              *")
        print("    /  \\▄▀           ▀▄/  \\        ║             *         ")
        print("*  /\\   █      0      █   /\\       ║          *           *")
        print("         ▀▄         ▄▀       *     ║     *          *       ")
        print("*     *    ▀▄▄▄▄▄▄▄▀      *        ║           *           *")
        print("\n")
    elif number_of_lives == 3:
        print("*           *                 *              *             *")
        print("    *                 *             *             \\|/      ")
        print("*          *                 *              *   -- O --    *")
        print("   *                              *               /|\\      ")
        print("*          *            *          ╔════════╗              *")
        print("*           *                 *    ║  HELP! ║     *         ")
        print("    *                              ║════════╝         *     ")
        print("*         █  x _ x  █     *        ║          *            *")
        print("      *    ▀▄▄▄▄▄▄▄▀               ║               *        ")
        print("*    /\\   ▄▀       ▀▄   /\\         ║        *              *")
        print("    /  \\▄▀           ▀▄/  \\        ║             *          ")
        print("         ▀▄         ▄▀       *     ║     *          *       ")
        print("*     *    ▀▄▄▄▄▄▄▄▀      *        ║           *           *")
        print("\n")
    elif number_of_lives == 2:
        print("*           *                 *              *             *")
        print("    *                 *             *             \\|/      ")
        print("*          *                 *              *   -- O --    *")
        print("   *              *               *               /|\\      ")
        print("*          *            *          ╔════════╗              *")
        print("      *           *           *    ║  HELP! ║       *       ")
        print("*                      *           ║════════╝              *")
        print("           *                       ║        *        *      ")
        print("*       *           *              ║             *          ")
        print("             x _ x        *        ║      *                *")
        print("*          ▀▄▄▄▄▄▄▄▀               ║               *        ")
        print("          ▄▀       ▀▄              ║        *              *")
        print("*     *    ▀▄▄▄▄▄▄▄▀      *        ║           *           *")
        print("\n")
    elif number_of_lives == 1:
        print("*           *                 *              *             *")
        print("    *                 *             *             \\|/      ")
        print("*          *                 *              *   -- O --    *")
        print("   *              *               *               /|\\      ")
        print("*          *            *          ╔════════╗              *")
        print("      *           *           *    ║  HELP! ║       *       ")
        print("*                      *           ║════════╝              *")
        print("           *                       ║                 *      ")
        print("*       *              *           ║             *          ")
        print("                *           *      ║        *              *")
        print("*       *           *              ║               *        ")
        print("             x _ x        *        ║      *                 ")
        print("*          ▀▄▄▄▄▄▄▄▀               ║               *       *")
        print("\n")
