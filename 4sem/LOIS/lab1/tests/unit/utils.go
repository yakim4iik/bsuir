package unittests

import (
	"bytes"
	"fmt"
	"reflect"
	"testing"
)

func AssertError(t *testing.T, err error) {
	if err == nil {
		t.Errorf("An error is expected but got nil.")
	}
}

func AssertNoError(t *testing.T, err error) {
	if err != nil {
		t.Errorf("got error %v, but must be nil", err)
	}
}

func objectsAreEqual(expected, actual interface{}) bool {
	if expected == nil || actual == nil {
		return expected == actual
	}

	exp, ok := expected.([]byte)
	if !ok {
		return reflect.DeepEqual(expected, actual)
	}

	act, ok := actual.([]byte)
	if !ok {
		return false
	}
	if exp == nil || act == nil {
		return exp == nil && act == nil
	}
	return bytes.Equal(exp, act)
}

func AssertEqual(t *testing.T, expected, actual interface{}) {
	if !objectsAreEqual(expected, actual) {
		t.Errorf("Not equal: \nexpected: %s\nactual  : %s", expected, actual)
	}
}

func AssertTrue(t *testing.T, value bool) {
	if !value {
		t.Errorf("Should be true")
	}
}

func AssertFalse(t *testing.T, value bool) {
	if value {
		t.Errorf("Should be false")
	}
}

func containsKind(kinds []reflect.Kind, kind reflect.Kind) bool {
	for i := 0; i < len(kinds); i++ {
		if kind == kinds[i] {
			return true
		}
	}

	return false
}

func isNil(object interface{}) bool {
	if object == nil {
		return true
	}

	value := reflect.ValueOf(object)
	kind := value.Kind()
	isNilableKind := containsKind(
		[]reflect.Kind{
			reflect.Chan, reflect.Func,
			reflect.Interface, reflect.Map,
			reflect.Ptr, reflect.Slice},
		kind)

	if isNilableKind && value.IsNil() {
		return true
	}

	return false
}

func AssertNil(t *testing.T, object interface{}) {
	if isNil(object) {
		return
	}

	t.Errorf(fmt.Sprintf("Expected nil, but got: %#v", object))
}
