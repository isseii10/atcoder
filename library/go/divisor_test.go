package library_test

import "testing"

func TestDivisor(t *testing.T) {
	tests := []struct{
		name string
		n int
		want []int
	}{
		{
			name: "10",
			n: 10,
			want: []int{1, 2, 5, 10}

		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := divisor(tt.n); got!=tt.want {
				t.Errorf("got=%v, want=%v", got, tt.want)
			}
		})
	}
}