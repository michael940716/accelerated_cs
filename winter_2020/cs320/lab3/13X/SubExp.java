class SubExp extends Exp {
  private Exp left;
  private Exp right;
  SubExp (Exp left, Exp right) {this.left = left; this.right = right;}


	void emit() {
			left.emit();
			right.emit();
      System.out.println("NEG");
      System.out.println("ADD");
	}

  int eval() {
    return left.eval() - right.eval();
  }
}
